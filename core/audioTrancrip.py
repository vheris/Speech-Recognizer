import whisper
import torch
import os

# Загружаем модель один раз при импорте
model = whisper.load_model("small", device="cuda" if torch.cuda.is_available() else "cpu")

def process_with_timestamps(current_file_path):
    try:
        # Транскрибация с таймкодами сегментов
        result = model.transcribe(current_file_path, verbose=True)
        
        # Создаем имя файла на основе исходного
        base_name = os.path.splitext(os.path.basename(current_file_path))[0]
        output_file = f"{base_name}.txt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
        
        return output_file
    except Exception as e:
        print(f"Ошибка транскрибации: {e}")
        return None

def process_without_timestamps(current_file_path):
    try:
        result = model.transcribe(current_file_path, verbose=True)
        
        base_name = os.path.splitext(os.path.basename(current_file_path))[0]
        output_file = f"{base_name}_text.txt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        return output_file
    except Exception as e:
        print(f"Ошибка транскрибации: {e}")
        return None

def process_as_subtitles(current_file_path):
    try:
        result = model.transcribe(current_file_path, verbose=True)
        
        base_name = os.path.splitext(os.path.basename(current_file_path))[0]
        output_file = f"{base_name}.srt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result["segments"], 1):
                start = format_time(segment["start"])
                end = format_time(segment["end"])
                text = segment["text"].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")
        
        return output_file
    except Exception as e:
        print(f"Ошибка создания субтитров: {e}")
        return None

def format_time(seconds):
    """Конвертирует секунды в формат SRT (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millisecs = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"