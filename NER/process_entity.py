results = [{'entity': 'O',
            'score': 0.99998426,
            'index': 1,
            'word': 'tôi',
            'start': 0,
            'end': 3},
           {'entity': 'O',
            'score': 0.999984,
            'index': 2,
            'word': 'tên',
            'start': 4,
            'end': 7},
           {'entity': 'O',
            'score': 0.99997616,
            'index': 3,
            'word': 'là',
            'start': 8,
            'end': 10},
           {'entity': 'B-PERSON',
            'score': 0.9998267,
            'index': 4,
            'word': 'Nguyễn',
            'start': 11,
            'end': 17},
           {'entity': 'I-PERSON',
            'score': 0.9998534,
            'index': 5,
            'word': 'Đức',
            'start': 18,
            'end': 21},
           {'entity': 'I-PERSON',
            'score': 0.9998493,
            'index': 6,
            'word': 'Minh',
            'start': 22,
            'end': 26},
           {'entity': 'O',
            'score': 0.99996984,
            'index': 7,
            'word': ',',
            'start': 26,
            'end': 27},
           {'entity': 'O',
            'score': 0.9999813,
            'index': 8,
            'word': 'sinh',
            'start': 28,
            'end': 32},
           {'entity': 'O',
            'score': 0.99998534,
            'index': 9,
            'word': 'năm',
            'start': 33,
            'end': 36},
           {'entity': 'O',
            'score': 0.99998236,
            'index': 10,
            'word': '2004',
            'start': 37,
            'end': 41},
           {'entity': 'O',
            'score': 0.9999833,
            'index': 11,
            'word': ',',
            'start': 41,
            'end': 42},
           {'entity': 'O',
            'score': 0.9999845,
            'index': 12,
            'word': 'học',
            'start': 43,
            'end': 46},
           {'entity': 'O',
            'score': 0.99998426,
            'index': 13,
            'word': 'ở',
            'start': 47,
            'end': 48},
           {'entity': 'B-LOCATION',
            'score': 0.99974567,
            'index': 14,
            'word': 'Phần',
            'start': 49,
            'end': 53},
           {'entity': 'I-LOCATION',
            'score': 0.99960357,
            'index': 15,
            'word': 'Lan',
            'start': 54,
            'end': 57},
           {'entity': 'O',
            'score': 0.9999839,
            'index': 16,
            'word': ',',
            'start': 57,
            'end': 58},
           {'entity': 'O',
            'score': 0.9999846,
            'index': 17,
            'word': 'sinh',
            'start': 59,
            'end': 63},
           {'entity': 'O',
            'score': 0.9999863,
            'index': 18,
            'word': 'ra',
            'start': 64,
            'end': 66},
           {'entity': 'O',
            'score': 0.9999865,
            'index': 19,
            'word': 'và',
            'start': 67,
            'end': 69},
           {'entity': 'O',
            'score': 0.9999862,
            'index': 20,
            'word': 'lớn',
            'start': 70,
            'end': 73},
           {'entity': 'O',
            'score': 0.9999865,
            'index': 21,
            'word': 'lên',
            'start': 74,
            'end': 77},
           {'entity': 'O',
            'score': 0.99998546,
            'index': 22,
            'word': 'ở',
            'start': 78,
            'end': 79},
           {'entity': 'B-LOCATION',
            'score': 0.9995983,
            'index': 23,
            'word': 'Hà',
            'start': 80,
            'end': 82},
           {'entity': 'I-LOCATION',
            'score': 0.99951947,
            'index': 24,
            'word': 'Nội',
            'start': 83,
            'end': 86}]


def process_entity(results):
    combined_entities = {}
    current_entity = []
    current_label = None

    for result in results:
        if '-B' in result['entity']:
            if current_entity:
                combined_entities[' '.join(
                    current_entity)] = current_label.split('-')[1]
                current_entity = []

                current_label = result['entity']
                current_entity.append(result['word'])
        elif 'I-' in result['entity'] and current_label and result['entity'].split('-')[1] == current_label.split('-')[1]:
            current_entity.append(result['word'])

        else:
            if current_entity:
                combined_entities[' '.join(
                    current_entity)] = current_label.split('-')[1]
                current_entity = []

            current_label = result['entity'] if 'B-' in result['entity'] else None
            if current_label:
                current_entity.append(result['word'])

    if current_entity:
        combined_entities[' '.join(current_entity)
                          ] = current_label.split('-')[1]

    return combined_entities


print(process_entity(results))
