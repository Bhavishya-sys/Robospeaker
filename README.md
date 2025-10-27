RoboSpeaker 1.1 is a simple Python-based text-to-speech (TTS) program that converts your typed text into speech.
Whatever you type, your computer will speak it aloud using the system’s built-in speech engine.

It’s a fun beginner project that demonstrates Python automation, OS commands, and voice synthesis.

🧠 How It Works

The program greets the user with a welcome message.

It repeatedly asks the user to type something.

Whatever the user types is spoken aloud by the computer.

Typing “q” quits the program.
⚙️ How It Works Internally

The program uses your system’s built-in speech engine through the os.system("say ...") command.

On Windows, you can replace say with powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('text here')"

On macOS, the say command works natively.

You can also use the pyttsx3 library (cross-platform) for smoother voice output.

🚀 Features

✅ Converts text to speech instantly
✅ Simple and lightweight
✅ Works offline
✅ Supports continuous input
✅ Beginner-friendly
