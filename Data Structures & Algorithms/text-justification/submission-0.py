class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        lenofline = 0

        i = 0

        while i < len(words):
            if lenofline + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                lenofline += len(words[i])
                i += 1
            else:
                spaces = maxWidth - lenofline
                gaps = len(line) - 1

                if gaps == 0:
                    newstring = line[0] + " " * spaces
                else:
                    spacespergap = spaces // gaps
                    extraspace = spaces % gaps

                    newstring = ""

                    for j in range(len(line)):

                        newstring += line[j]

                        if j < gaps:
                            numberofspaces = spacespergap
                            if j < extraspace:
                                numberofspaces += 1

                            newstring += " " * numberofspaces


                result.append(newstring)

                line = []
                lenofline = 0

        lastline = " ".join(line)
        lastline += " " * (maxWidth - len(lastline))
        result.append(lastline)

        return result


