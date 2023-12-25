"""
Hometask 04 Сount vowels.

The English language has five vowels: A, E, I, O, and U
Please count each vowel occurrence in text bellow
(total sum of lower and capital cases)
and write output as table smth like this
-----------------
| vowel | count |
-----------------
|   a   |  11   |
|   e   |  23   |
-----------------

then modify text where each vowel replaced with
A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
ex. "Í wàndéréd lónély...."   and print it

poem_text = I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""
count_of_a = poem_text.count('a') + poem_text.count('A')
count_of_e = poem_text.count('e') + poem_text.count('E')
count_of_i = poem_text.count('i') + poem_text.count('I')
count_of_o = poem_text.count('o') + poem_text.count('O')
count_of_u = poem_text.count('u') + poem_text.count('U')
print(f"""
 -----------------
 | vowel | count |
 -----------------
 |   a   |  {count_of_a}   |
 |   e   |  {count_of_e}   |
 |   i   |  {count_of_i}   |
 |   o   |  {count_of_o}   |
 |   u   |  {count_of_u}    |
""")
translation_table = str.maketrans('AaEeIiOoUu', 'ÀàÉéÍíÓóÚú')
modified_poem = poem_text.translate(translation_table)
print(modified_poem)
