import pywhatkit as pw

txt = """A quotation is the repetition of a sentence, 
phrase, or passage from speech or text that someone has said or written. 
In oral speech, it is the representation of an utterance that is 
introduced by a quotative marker, such as a verb of saying."""

pw.text_to_handwriting(txt, "demo.png", [255,0,0])

print("  END  ")

