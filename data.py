from googletrans import Translator

translator = Translator()

def thrips(lang):
    a = []
    a.append('Leaf shows discolorationand rolling')
    a.append('Yellow (or) silvery streaks on the leaves of young seedlings')
    a.append('Terminal rollingand drying of leaves from tip to base')
    a.append('It causes damage both in nurseryand main field')
    a.append('Leaf tips wither off when severely infested')
    a.append('Unfilled grainsat panicle stage')

    b = []
    b.append('Spray Phosphamidon 40 SL 50 ml')
    for i in a:
        i = translator.translate(i,dest=lang)
    for i in b:
        i = translator.translate(i,dest=lang)
    return a,b

def greenlhop(lang):
    a = []
    a.append('Yellowing of leaves from tip to downwards')
    a.append('Vector for the diseases viz., Rice tungro virus, rice yellow & transitory yellowing cause direct damage to the rice plant')
    a.append('Retarded vigorous and stunted growth')
    a.append('Drying up of plant due to sucking up of the leaf')

    b = []
    b.append('Phosphamidon 40 SL 50 ml')
    b.append('Phosalone 35 EC 120 ml')
    for i in a:
        i = translator.translate(i,dest=lang)
    for i in b:
        i = translator.translate(i,dest=lang)
    return a,b

def ricecase(lang):
    a = []
    a.append('Caterpillars feed on green tissues of the leaves and leave become whitish papery')
    a.append('Tubular cases around the tillers by cutting the apical portion of leaves')
    a.append('Floating of tubular cases on the water')
    a.append('Cutting off leaf tips to make leaf cases')

    b = []
    b.append('Mix 250 ml of kerosene to the standing water')
    b.append('Dislodge the cases by passing a rope and drain water. Collect the cases and destroy')
    b.append('Spray Quinalphos 25 EC 80 ml')
    for i in a:
        i = translator.translate(i,dest=lang)
    for i in b:
        i = translator.translate(i,dest=lang)
    return a,b

def padstem(lang):
    a = []
    a.append('Presence of brown coloured egg mass near leaf tip')
    a.append('Caterpillar bore into central shoot of paddy seedling and tiller, causes drying of the central shoot known as “dead heart”')
    a.append('Grown up plant whole panicle becomes dried “white ear”')
    a.append('Plants could be easily pulled by hand')

    b = []
    b.append('Trichogramma japonicum  for the management of the rice yellow stem borer')
    b.append('Spraying Neem seed kernel extract controls stem bore')
    b.append('Clip the seedling tips before transplanting to eliminate egg masses and collect and destroy the egg masses in main field')
    for i in a:
        i = translator.translate(i,dest=lang)
    for i in b:
        i = translator.translate(i,dest=lang)
    return a,b

def gallmidge(lang):
    a = []
    a.append('Maggot feeds at the base of the growing shoot')
    a.append('Caterpillar bore into central shoot of paddy seedling and tiller, causes drying of the central shoot known as “dead heart”')
    a.append('Infested tillers produce no panicles.')

    b = []
    b.append('Release Platygaster oryzae parasitised galls at 1/10 m2 on 10 days after transplanting (DAT)')
    b.append('Optimum recommendation of potash fertilizer')
    b.append('Phosalone 35 EC 1500 ml/ha')
    for i in a:
        i = translator.translate(i,dest=lang)
    for i in b:
        i = translator.translate(i,dest=lang)
    return a,b