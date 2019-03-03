import wikipedia
import nltk

def get_slogan(topic):
    try:
        text=wikipedia.summary(topic)
    except:
        text='a'
    # print(text)


    text = nltk.word_tokenize(text)
    # print(text)
    tagged = nltk.pos_tag(text)

    found_verb=False
    slogan="0"
    for i,tag in enumerate(tagged):

        if tag[1]=="VB" and found_verb==False:
            found_verb=True
        elif (tag[1]=="NN" or tag[1]=="JJ") and found_verb==True:
            slogan=tagged[i-1][0]+" "+tagged[i][0]+"!"
            break
        else:
            found_verb=False

    if len(slogan)>1:
        # print(slogan)
        k=1
    else:
        # print("Not found.")
        k=2

    return slogan


def is_ascii(s):
    return all(ord(c) < 128 for c in s)
def remove_nonascii(mlist):
    new_list=[]
    for i in range(0,len(mlist)):
        is_good=is_ascii(mlist[i])
        if is_good:
            new_list.append(mlist[i])

    return new_list

N=2000
topics=wikipedia.random(pages=N)
topics=remove_nonascii(topics)
N=len(topics    )
meme_list=[]
for i in range(0,N):
    slogan = get_slogan(topics[i])
    if slogan!='0':
        meme=slogan+"   (from "+topics[i]+')'
        print(meme)
        meme_list.append(meme)
meme_list=remove_nonascii(meme_list)

from img_search import get_image
from memegenerator import make_meme
image_topics=wikipedia.random(pages=2*N)
image_topics=remove_nonascii(image_topics)

for i in range(len(meme_list)):
    img_topic=image_topics[i]
    try:
        get_image(img_topic )
        make_meme("Keep calm and ",meme_list[i],img_topic+".jpg")
    except:
        k=1
