from json import dump

wool_to_string_base = {
    'type': 'minecraft:crafting_shapeless',
    'ingredients': [
        {
            'tag': 'minecraft:wool',
            'count': 1
        }
    ],
    'result': {
        'item': 'minecraft:string', 
        'count': 4
    }
}

data_base = lambda color: {
    'wool': {
        'type': 'crafting_shapeless',
        'group': 'ct:color_wool',
        'ingredients': [
            {
                'tag': 'minecraft:wool',
                'count': 1
            },
            {
                'item': f'minecraft:{color}_dye',
                'count': 1
            }
        ],
        'result': {
            'item': f'minecraft:{color}_wool',
            'count': 1
        }
    },
    'bed': {
        'type': 'minecraft:crafting_shapeless',
        'group': 'ct:color_bed',
        'ingredients': [
            {
                'tag': 'wool_tweaks:wt_bed',
                'count': 1
            },
            {
                'item': f'minecraft:{color}_dye',
                'count': 1
            }
        ],
        'result': {
            'item': f'minecraft:{color}_bed',
            'count': 1
        }
    },
    'carpet': {
        'type': 'minecraft:crafting_shaped',
        'group': 'ct:color_carpet',
        'pattern': [
            '***',
            '*_*',
            '***'
        ],
        'key': {
            '*': {
                'tag': '#wool_tweaks:carpets'
            },
            '_': {
                'item': f'minecraft:{color}_dye'
            }
        },
        'result': {
            'item': f'minecraft:{color}_carpet',
            'count': 8
        }
    }
}

def dump_file(path: str, data: dict) -> None:
    with open(f'./Wool Tweaks/data/wool_tweaks/recipes/{path}.json', mode='w') as file:
        dump(data, file, indent=4)

dump_file('wool_to_string', wool_to_string_base)

for color in {'red', 'black', 'blue', 'brown', 
              'cyan', 'gray', 'green', 'light_blue', 
              'light_gray', 'lime', 'magenta', 'orange', 
              'pink', 'purple', 'white', 'yellow'}:
    for path, data in data_base(color).items():
        dump_file(f'{path}/{color}_{path}', data)