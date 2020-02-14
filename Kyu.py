def alphabet_position(text):
    hollow = ''
    for x in text:
        if x == 'A' or x == 'a':
            hollow += '1' + ' ';
        elif x == 'B' or x == 'b':
            hollow +=  '2' + ' ';
        elif x == 'C' or x == 'c':
            hollow +=  '3' + ' ';
        elif x == 'D' or x == 'd':
            hollow +=  '4' + ' ';
        elif x == 'E' or x == 'e':
            hollow +=  '5' + ' ';
        elif x == 'F' or x == 'f':
            hollow +=  '6' + ' ';
        elif x == 'G' or x == 'g':
            hollow +=  '7' + ' ';
        elif x == 'H' or x == 'h':
            hollow +=  '8' + ' ';
        elif x == 'I' or x == 'i':
            hollow +=  '9' + ' ';
        elif x == 'J' or x == 'j':
            hollow +=  '10' + ' ';
        elif x == 'K' or x == 'k':
            hollow +=  '11' + ' ';
        elif x == 'L' or x == 'l':
            hollow +=  '12' + ' ';
        elif x == 'M' or x == 'm':
            hollow +=  '13' + ' ';
        elif x == 'N' or x == 'n':
            hollow +=  '14' + ' ';
        elif x == 'O' or x == 'o':
            hollow +=  '15' + ' ';
        elif x == 'P' or x == 'p':
            hollow +=  '16' + ' ';
        elif x == 'Q' or x == 'q':
            hollow +=  '17' + ' ';
        elif x == 'R' or x == 'r':
            hollow +=  '18' + ' ';
        elif x == 'S' or x == 's':
            hollow +=  '19' + ' ';
        elif x == 'T' or x == 't':
            hollow +=  '20' + ' ';
        elif x == 'U' or x == 'u':
            hollow +=  '21' + ' ';
        elif x == 'V' or x == 'v':
            hollow +=  '22' + ' ';
        elif x == 'W' or x == 'w':
            hollow +=  '23' + ' ';
        elif x == 'X' or x == 'x':
            hollow +=  '24' + ' ';
        elif x == 'Y' or x == 'y':
            hollow +=  '25' + ' ';
        elif x == 'Z' or x == 'z':
            hollow +=  '26' + ' ';
    s = list(hollow)
    del s[len(hollow) - 1]
    return "".join(s)






