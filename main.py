from deepface import DeepFace
import json

def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        if result_dict['verified']:
            result_dict['verified'] = str(result_dict['verified'])
            with open('result.json', 'w') as file:
                json.dump(result_dict, file, indent=4, ensure_ascii=False)

        # return result_dict
        if result_dict.get('verified'):
            return 'Проверка пройдена. Пропустить.'
        return 'Нарушитель! Задержать!!'

    except Exception as _ex:
        return _ex
    

def face_recogn():
    try:
        result = DeepFace.find(img_path='faces/kurt-1.jpeg', db_path='kurt')
        result = result[0].values.tolist()
        return result

    except Exception as _ex:
        return _ex

def face_analyze():
    try:
        # result_dict = DeepFace.analyze(img_path='faces/robert.jpg', actions=['age', 'gender', 'race', 'emotion'])
        result_dict = DeepFace.analyze(img_path='faces/i.jpg', actions=['age', 'gender', 'race', 'emotion'])

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)
        result = result_dict[0]

        print(f"[+] Age: {result.get('age')}")
        print(f'[+] Gender: {result["gender"]}')
        print('[+] Race:')

        for k, v in result.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

        # return result_dict

    except Exception as _ex:
        return _ex

def main():
    # print(face_verify(img_1='faces/Klark-1.jpg', img_2='faces/Leo-Messi.jpg'))
    # print(face_recogn())
    face_analyze()

if __name__ == '__main__':
    main()