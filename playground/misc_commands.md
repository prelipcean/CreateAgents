# MISC COMMANDS

## UV 

Check if uv envrionment is running, pip list in uv env and python path

```
BASH: echo $VIRTUAL_ENV
DOS:  echo %VIRTUAL_ENV%
PS:   $Env:VIRTUAL_ENV
uv pip list
which python
```

### Langchain version

```
uv pip show langchain
```

## Run scripts

```
e.g. python <path_python_file>
```

## Ollama

Ollama install https://ollama.com after installation check: http://localhost:11434 to see the message "Ollama is running"

### Commands

```
ollama pull <model_name> 
ollama ls 
ollama rm <model_name>
```

## GIT

### Revert to last commit after push on remote

```
git reset --hard HEAD~1
git push origin HEAD --force
```

## GOOGLE GEMINI

### Available Gemini Models that support 'generateContent'

--------------------------------------------------
Model: models/gemini-1.0-pro-vision-latest
Display Name: Gemini 1.0 Pro Vision
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-pro-vision
Display Name: Gemini 1.0 Pro Vision
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-pro-latest
Display Name: Gemini 1.5 Pro Latest
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-pro-002
Display Name: Gemini 1.5 Pro 002
Supported Methods: generateContent, countTokens, createCachedContent
--------------------------------------------------
Model: models/gemini-1.5-pro
Display Name: Gemini 1.5 Pro
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-flash-latest
Display Name: Gemini 1.5 Flash Latest
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-flash
Display Name: Gemini 1.5 Flash
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-flash-002
Display Name: Gemini 1.5 Flash 002
Supported Methods: generateContent, countTokens, createCachedContent
--------------------------------------------------
Model: models/gemini-1.5-flash-8b
Display Name: Gemini 1.5 Flash-8B
Supported Methods: createCachedContent, generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-flash-8b-001
Display Name: Gemini 1.5 Flash-8B 001
Supported Methods: createCachedContent, generateContent, countTokens
--------------------------------------------------
Model: models/gemini-1.5-flash-8b-latest
Display Name: Gemini 1.5 Flash-8B Latest
Supported Methods: createCachedContent, generateContent, countTokens
--------------------------------------------------
Model: models/gemini-2.5-pro-preview-03-25
Display Name: Gemini 2.5 Pro Preview 03-25
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash-preview-04-17
Display Name: Gemini 2.5 Flash Preview 04-17
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash-preview-05-20
Display Name: Gemini 2.5 Flash Preview 05-20
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash
Display Name: Gemini 2.5 Flash
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash-preview-04-17-thinking
Display Name: Gemini 2.5 Flash Preview 04-17 for cursor testing
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash-lite-preview-06-17
Display Name: Gemini 2.5 Flash-Lite Preview 06-17
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-pro-preview-05-06
Display Name: Gemini 2.5 Pro Preview 05-06
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-pro-preview-06-05
Display Name: Gemini 2.5 Pro Preview
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-pro
Display Name: Gemini 2.5 Pro
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-exp
Display Name: Gemini 2.0 Flash Experimental
Supported Methods: generateContent, countTokens, bidiGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash
Display Name: Gemini 2.0 Flash
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-001
Display Name: Gemini 2.0 Flash 001
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-lite-001
Display Name: Gemini 2.0 Flash-Lite 001
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-lite
Display Name: Gemini 2.0 Flash-Lite
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-lite-preview-02-05
Display Name: Gemini 2.0 Flash-Lite Preview 02-05
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-lite-preview
Display Name: Gemini 2.0 Flash-Lite Preview
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-pro-exp
Display Name: Gemini 2.0 Pro Experimental
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-pro-exp-02-05
Display Name: Gemini 2.0 Pro Experimental 02-05
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-exp-1206
Display Name: Gemini Experimental 1206
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-thinking-exp-01-21
Display Name: Gemini 2.5 Flash Preview 04-17
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-thinking-exp
Display Name: Gemini 2.5 Flash Preview 04-17
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.0-flash-thinking-exp-1219
Display Name: Gemini 2.5 Flash Preview 04-17
Supported Methods: generateContent, countTokens, createCachedContent, batchGenerateContent
--------------------------------------------------
Model: models/gemini-2.5-flash-preview-tts
Display Name: Gemini 2.5 Flash Preview TTS
Supported Methods: countTokens, generateContent
--------------------------------------------------
Model: models/gemini-2.5-pro-preview-tts
Display Name: Gemini 2.5 Pro Preview TTS
Supported Methods: countTokens, generateContent
--------------------------------------------------
Model: models/learnlm-2.0-flash-experimental
Display Name: LearnLM 2.0 Flash Experimental
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3-1b-it
Display Name: Gemma 3 1B
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3-4b-it
Display Name: Gemma 3 4B
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3-12b-it
Display Name: Gemma 3 12B
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3-27b-it
Display Name: Gemma 3 27B
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3n-e4b-it
Display Name: Gemma 3n E4B
Supported Methods: generateContent, countTokens
--------------------------------------------------
Model: models/gemma-3n-e2b-it
Display Name: Gemma 3n E2B
Supported Methods: generateContent, countTokens
--------------------------------------------------
