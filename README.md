# basic-voice-chatbot

A very basic voicechatbot using openai

This code was tested on Ubuntu 22.04 Desktop and using Python 3.10.6

### Instructions:

## MacOS

```shell
# Install flac
brew install flac

# Install PyAudio
brew install portaudio
pyaudio_path=$(dirname $(brew list -1 portaudio | head -n 1))

# Install requirements with required global options
pip3 install --global-option='build_ext' --global-option="-I${pyaudio_path}/include" --global-option="-L${pyaudio_path}/lib" -r requirements.txt
```

## Ubuntu:

```shell
sudo apt-get install python3-pyaudio
pip3 install -r requirements.txt
```

## Run the script:

```shell
# Run the script
python3 main.py
```
