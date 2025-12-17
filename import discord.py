import discord
from discord.ext import commands
#from model import get_class
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
listaPrzyklad = ["Segreguj śmieci - $trash", "Oszczędzaj wodę - $water", "Oszczędzaj energię - $energy", "Buduj nawyki ZERO WASTE - $zerowaste", 
"Wprowadzaj elementy diet wegetariańskich i wegańskich - $wege", "Ogranicz zużycie plastiku i papieru - $waste", "Dbaj o przyrodę - $nature", 
"Ogranicz korzystanie z samochodu - $car", "Korzystaj z odnawialnych źródeł energii - $reborn", "Edukuj innych - $edu"]
listaTrash = ["Oszczędzaj papier, zbieraj makulaturę.", "Używaj butelek zwrotnych, szkło wyrzucaj do specjalnie oznaczonych pojemników.", 
"Unikaj kupowania rzeczy z plastiku, na zakupy zabieraj ze sobą reklamówki.", 
"Zużyte baterie umieszczaj w specjalnie oznaczonych do tego celu miejscach.", "Nie wyrzucaj do śmieci opakowań po farbach czy rozpuszczalnikach.",
"Kupuj artykuły w szkle."]
listaWater = ["Korzystaj z kąpieli pod prysznicem zamiast w wannie.", "W spłuczce w toalecie załóż zawór ograniczający.",
"Ogranicz pranie.", "Oszczędzaj wodę przy zmywaniu.", "Kontroluj szczelność kranów.", "Kupuj sprzęty oszczędzające wodę."]
listaEnergy = ["Dostosuj temperaturę do potrzeb. Optymalna wynosi 20–21 stopni Celsjusza.", "Wyłączaj systemy grzewcze podczas wietrzenia."
"Nie zostawiaj urządzeń w trybie standby. Zaoszczędzisz w ten sposób 62 zł rocznie.", "Zamontuj na kaloryferach termostaty.",
"Pierz dopiero gdy jest pełny ładunek prania.", "Wymień żarówki na energooszczędne."]
listaZeroWaste = ["Nie przyjmuj darmowych gadżetów, zbytecznych prezentów, dodatkowych opakowań czy niepotrzebnych zabawek dla dzieci.",
"Świadomie kupuj tylko tyle, ile dokładnie potrzebujesz.","Staraj się znaleźć zastosowanie dla starych rzeczy, naprawiaj je albo oddaj komuś, komu mogą się przydać.",
"Dbaj o właściwą segregację śmieci.", "Utylizuj surowce podlegające rozkładowi. Kompost może zastąpić sztuczne pestycydy, a więc przyczyniać się do zdrowszych upraw."]
listaWege = ["Zastąp produkty mięsne ich roślinnymi odpowiednikami.", "Naucz się przyrządzać nowe potrawy z warzyw.", "Dowiedz się, jak komponować zdrowe posiłki na diecie wegańskiej i wegetariańskiej."]
listaWaste = ["Rób zakupy z materiałową torbą.", "Zamień wodę butelkowaną na wodę z kranu.", "Kupuj kosmetyki naturalne w opakowaniach nadających się do recyklingu.",
"Kupuj produkty na wagę.", "Nie drukuj, jeśli nie musisz, albo drukuj dwustronnie.", "Wybieraj rachunki oraz faktury w wersji elektronicznej.", 
"Czytaj książki i gazety w wersji elektronicznej."]
listaNature = ["Oszczędzaj energię i wodę.", "Segreguj śmieci.", "Szanuj zwierzęta.", "Nie śmieć.", "Zrezygnuj z jednorazowych opakowań.", "Zmień dietę.", "Zacznij uprawiać plogging (czyli bieganie połączone ze zbieraniem śmieci)."]
listaCar = ["Jeśli masz taką możliwość, wybierz środki transportu publicznego, rower lub… użyj własnych nóg.",
"W dalsze podróże wybieraj się raczej pociągiem niż autobusem, samolotem czy promem.",
"Jeśli jeździsz autem, używaj samochodu posiadającego filtry cząstek stałych, które pozwalają oddzielać sadzę od spalin samochodowych.",
"Używaj takich rozwiązań jak reaktor katalityczny, bezpośredni wtrysk paliwa czy system EGR w samochodzie."]
listaReborn = ["Podgrzewaj wodę użytkowa energią z kolektorów słonecznych.", "Ogrzewaj dom za pomocą pomp ciepła.", "Stosuj panele fotowoltaiczne jako źródło prądu."]
listaEdu = ["Rozmawiaj ze swoimi dziećmi, jak dbać o środowisko.", "Wprowadzaj ekologiczne nawyki we własnym domu.", "Zachęcaj znajomych do działań na rzecz ochrony środowiska.", 
"Zachęcaj do zmiany diety, nawyków, świadomego kupowania, oszczędzania wody i energii.", "Organizuj wspólne spędzanie czasu bez używania samochodu, promuj piesze i rowerowe wycieczki z rodziną i przyjaciółmi."]

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def helpEnv(ctx):
    await ctx.send(f'Wylosowuję temat dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaPrzyklad))

@bot.command()
async def trash(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaTrash))

@bot.command()
async def water(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaWater))

@bot.command()
async def energy(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaEnergy))

@bot.command()
async def zerowaste(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaZeroWaste))

@bot.command()
async def wege(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaWege))

@bot.command()
async def waste(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaWaste))

@bot.command()
async def nature(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaNature))

@bot.command()
async def car(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaCar))

@bot.command()
async def reborn(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaReborn))

@bot.command()
async def edu(ctx):
    await ctx.send(f'Wylosowuję pomysł dla Ciebie...')
    await asyncio.sleep(2)
    await ctx.send(random.choice(listaEdu))




bot.run("token")