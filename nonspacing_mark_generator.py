import random
from codeset import nonspacing_mark_codeset

print(len(nonspacing_mark_codeset))

def nonspacing_mark_generator(text, num_nonspacing_mark=1):
    out_text = ''
    for c in text:
        nm=''.join(chr(int(nonspacing_mark_codeset[random.randrange(268)],16)) for i in range(num_nonspacing_mark))
        out_text+= c+nm
    return out_text
        

if __name__ == '__main__':
    text = 'The new generator haha'
    print(nonspacing_mark_generator(text, num_nonspacing_mark=1))
