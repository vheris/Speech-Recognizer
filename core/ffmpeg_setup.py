import os
import sys
import subprocess
import platform

def check_ffmpeg():
    """Проверяет наличие FFmpeg в системе"""
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ffmpeg():
    """Пытается установить FFmpeg автоматически"""
    system = platform.system().lower()
    
    try:
        if system == "darwin":  # macOS
            # Проверяем наличие Homebrew
            subprocess.run(['brew', '--version'], 
                          stdout=subprocess.DEVNULL, 
                          stderr=subprocess.DEVNULL, 
                          check=True)
            subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
            return True
            
        elif system == "linux":
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'ffmpeg'], check=True)
            return True
            
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    
    return False

def setup_ffmpeg():
    """Основная функция настройки FFmpeg"""
    if check_ffmpeg():
        print("FFmpeg уже установлен")
        return True
    
    print("FFmpeg не найден. Попытка автоматической установки...")
    
    if install_ffmpeg():
        if check_ffmpeg():
            print("FFmpeg успешно установлен!")
            return True
        else:
            print("Ошибка: FFmpeg не работает после установки")
            return False
    else:
        print("Не удалось установить FFmpeg автоматически")
        print("Пожалуйста, установите FFmpeg вручную:")
        
        system = platform.system().lower()
        if system == "darwin":
            print("macOS: brew install ffmpeg")
        elif system == "linux":
            print("Ubuntu/Debian: sudo apt install ffmpeg")
        elif system == "windows":
            print("Windows: скачайте с https://ffmpeg.org")
        
        return False

if __name__ == "__main__":
    setup_ffmpeg()