def insert_white_space(sentence):
    sentence_2 = []
    print(type(sentence_2))
    for element in sentence:
        if element.isupper():
            sentence_2.append(f" {element}")
        else:
            sentence_2.append(element)
    sentence_2 = "".join(sentence_2)
    return sentence_2


print(insert_white_space("WhoWantsToDoBadThings?"))
