from formatter import Formatter

text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.'
# text = 'And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'
size = 40
justify = False

f = Formatter()

if justify:
    justified = f.justify(text, size)
    f.save_file(justified)

else:
    split = f.fast_split(text, size)
    f.save_file(split)