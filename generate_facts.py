import argparse
import random
import string
from typing import Union

CARDINALITIES_OPTIONS = [
    'one',
    'many',
]

OPERATION_OPTIONS = [
    True,
    False,
    True,
]

SchemaFact = tuple[str, str, str]
FactValue = Union[str, int]
Fact = tuple[str, str, FactValue, bool]


def generate_attributes_schema(how_many: int = 5) -> list[SchemaFact]:
    schema: list[SchemaFact] = []

    for index in range(how_many):
        schema.append((f'attribute_{index}', 'cardinality',
                       random.choice(CARDINALITIES_OPTIONS)))

    return schema


def generate_facts(schema: list[SchemaFact],
                   how_many_entities: int = 5,
                   how_many_facts: int = 10,
                   value_length: int = 10) -> list[Fact]:

    facts: list[Fact] = []

    for _ in range(how_many_facts):
        facts.append((
            gen_entity_name(how_many_entities),
            gen_attribute_name(schema),
            gen_value(value_length),
            random.choice(OPERATION_OPTIONS),
        ))

    return facts


def gen_entity_name(how_many_entities: int) -> str:
    return f'entity_{random.randint(0, how_many_entities)}'


def gen_attribute_name(schema: list[SchemaFact]) -> str:
    schema_fact = random.choice(schema)
    return schema_fact[0]


def gen_value(value_length:int=10) -> FactValue:
    if random.randint(0, 1):
        return random.randint(0, 10000)
    else:
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=value_length))


def create_file(schema: Union[list[SchemaFact], list[Fact]], file_name: str):
    with open(file_name, 'w') as file:
        for fact in schema:
            line = ''
            for fact_index in range(len(fact) - 1):
                line += f'{fact[fact_index]}---'
            line += f'{fact[len(fact) - 1]}\n'

            file.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script to generate facts and schema facts.')

    parser.add_argument('-as', '--attributes_size',
                        action='store',
                        default=10,
                        type=int,
                        help='number of possible attributes (default: 10)')
    
    parser.add_argument('-es', '--entities_size',
                        action='store',
                        default=5,
                        type=int,
                        help='number of possible entities (default: 10)')
    
    parser.add_argument('-fs', '--facts_size',
                        action='store',
                        default=100,
                        type=int,
                        help='define the number of facts to be generated (default: 100)')

    parser.add_argument('-vs', '--values_size',
                        action='store',
                        default=10,
                        type=int,
                        help='define the string length of fact values (default: 10)')

    args = parser.parse_args()

    schema = generate_attributes_schema(args.attributes_size)
    facts = generate_facts(schema, args.entities_size, args.facts_size, args.values_size)

    create_file(schema, 'schema.txt')
    create_file(facts, 'facts.txt')