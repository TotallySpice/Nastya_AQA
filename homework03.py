"""03 homework."""
norway_text = ('Automatisering akselererer %syeblikket da roboter vil erobre '
               'planeten v%sr. (%s)' % ('ø', 'å', 'Æ'))
print(norway_text)
# rewrate with format()
norway_text1 = ('Automatisering akselererer {0}yeblikket da roboter vil '
                'erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ'))
print(norway_text1)
# rewrate with f-string
norway_text2 = f'Automatisering akselererer {'ø'}yeblikket da roboter  vil '
f'erobre planeten v{'å'}r. ({'Æ'})'
print(norway_text2)
