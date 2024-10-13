# Course-Digitalization

## Approach
- Video to audio(moviepy)
- <s>Azure speech to text to get transcript</s> Using Whisper to get transcript
- From transcript extract:
    - Pre-read(what will be discussed in the video)
    - Summary(What happened in the video, a little more detailed that pre-read)
    - <s>10 FAQs of recall-from-content type(currently one prompt, can breakdown to 10 questions and generate options separately: more control)</s>
    - Breakdown the content into sections and have section level 3 4 MCQs


## Ideas:
- Divide content of the video to sections
- Have MCQs popping up after that section completes(Maybe one at the end too)
- Each answer/reference/chat bot must be associated withthe time stamp of the reference made from video - Gives the feel of authenticity to the viewer
- Can have a few short answer type questions and use LLM to evaluate
- Finally questions to solve - We won't give solution unless they request