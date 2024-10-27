from pytubefix import YouTube
import sys, os
import argparse

def download(link: str, target_folder: str = '.'):
    # Substitua 'URL_DO_VIDEO' pela URL do vídeo que você deseja baixar
    url = link
    try:
        youtube = YouTube(url)
        # Baixe o vídeo em alta qualidade
        youtube.streams.get_highest_resolution().download(target_folder)
    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Download videos from YouTube')
    parser.add_argument('-f', '--target', type=str, help='Target Folder')
    parser.add_argument('-u', '--urls', type=str, nargs='+', help='URL of the video')
    args = parser.parse_args()

    if args.target:
        target_folder = args.target
    else:
        target_folder = '.'

    if args.urls:
        for url in args.urls:
            download(url, target_folder)
    else:
        print('No URL provided')
        sys.exit(1)

if __name__ == '__main__':
    main()
