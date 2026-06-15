def chunk_text(text):
    chunked_text = []
    cursor =0
    for cursor in range(0, len(text), 450):
        chunked_text.append(text[cursor:cursor+500])
        cursor+=450
    return chunked_text

if __name__ == "__main__":
    ex_text= """ [Block01--][Block02--][Block03--][Block04--][Block05--][Block06--][Block07--][Block08--][Block09--][Block10--][Block11--][Block12--][Block13--][Block14--][Block15--][Block16--][Block17--][Block18--][Block19--][Block20--][Block21--][Block22--][Block23--][Block24--][Block25--][Block26--][Block27--][Block28--][Block29--][Block30--][Block31--][Block32--][Block33--][Block34--][Block35--][Block36--][Block37--][Block38--][Block39--][Block40--][Block41--][Block42--][Block43--][Block44--][Block45--][Block46--][Block47--][Block48--][Block49--][Block50--][Block51--][Block52--][Block53--][Block54--][Block55--][Block56--][Block57--][Block58--][Block59--][Block60--][Block61--][Block62--][Block63--][Block64--][Block65--][Block66--][Block67--][Block68--][Block69--][Block70--][Block71--][Block72--][Block73--][Block74--][Block75--][Block76--][Block77--][Block78--][Block79--][Block80--][Block81--][Block82--][Block83--][Block84--][Block85--][Block86--][Block87--][Block88--][Block89--][Block90--][Block91--][Block92--][Block93--][Block94--][Block95--][Block96--][Block97--][Block98--][Block99--][Block100-] """
    ct = chunk_text(ex_text)
    print(len(ct))
    print(len(ex_text))
    print(ct)