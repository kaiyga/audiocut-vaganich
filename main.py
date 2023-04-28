from pydub import AudioSegment
import os
import sys
import asyncio

def cutting(filename = ''):
    if filename != '':
        pass
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input('[Имя файла, который вы хотите разбить]>>')
    name = filename.split('.')[0]
    format = filename.split('.')[1]
    folder = name+'_audio'
    chunk_length = 10000 # 10 секунд в млс
    #Открываю аудио
    audio_file = AudioSegment.from_file(f"{filename}", format=format)
    chunks = list(audio_file[::chunk_length])
    # Создаем папку для сохранения кусков
    if not os.path.exists(folder):
        os.mkdir(folder)
    # Сохраняем 
    for i, chunk in enumerate(chunks):
        chunk_name = f"{name}{i}.{format}"
        chunk.export(os.path.join(folder, chunk_name), format=f"{format}")


async def async_cutting(filename = ''):
    if filename != '':
        pass
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input('[Имя файла, который вы хотите разбить]>>')
    name = filename.split('.')[0]
    format = filename.split('.')[1]
    folder = name+'_audio'
    chunk_length = 10000 # 10 секунд в млс
    #Открываю аудио
    audio_file = AudioSegment.from_file(f"{filename}", format=format)
    chunks = list(audio_file[::chunk_length])
    # Создаем папку для сохранения кусков
    if not os.path.exists(folder):
        os.mkdir(folder)
    # Сохраняем 
    for i, chunk in enumerate(chunks):
        chunk_name = f"{name}{i}.{format}"
        chunk.export(os.path.join(folder, chunk_name), format=f"{format}")

asyncio.run(async_cutting(filename=''))