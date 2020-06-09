#### interfaces

**transcriberinterface:** provide method stubs for what transcriber does. at least a `transcribe()` method

**processors:** provide methods that process the transcriptions via NLP



#### transcribers:

- batch transcriber transcribes a batch of string
- streaming transcriber transcribers a stream of strings



#### processors

- processes with basic recognition 
- processes with advanced recorgnition 



#### `Application.py`

singleton that executes the classes in the combination they are wanted



#### `main.py`

loads `application.py` with args

