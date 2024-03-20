# Esitellään luokka
class Player:
    # staattinen eli luokkamuuttuja (arvo jaetaan olioiden kesken)
    player_count = 0
    #self viittaa aina olioon itseensä
    def __init__(self, name, start_location= 'Suomi'):
        Player.player_count = Player.player_count + 1
        print(f"Luodaan uusi peleeja {Player.player_count} kpl")
        self.name = name
        self.score = 0
        self.level = 1
        self.location = start_location

    def move_to_location(self, target):
        self.location = target

    def upgrade_level(self):
        self.level = self.level + 1

    def add_score(self):
        self.score += self.level * 10

    def print_info(self):
        print(f'{self.name} ({self.location}) pisteet {self.score}')

p1 = Player('john', 'Suomi')
p2 = Player('Jane', 'Ruotsi')
p3 = Player('Mary' )

# staattisiin muuttujiin viitataan luokan nimen avulla
print(Player.player_count)

# yleensä huono tapa muuttaa olion ominaisuukksia suoraan ulkopuolelta
# p3.score = 16

p2.add_score()      # +10
p2.upgrade_level()  #
p2.add_score()      # + 20p

# kutsutaan jonkun olion metodia
p2.move_to_location('Tanksa')

# p4 viittaa samaan Player-olioon kuin p1
p4 = p1
# p1.name = "john"

print(f'{p1.name} ({p1.location}) pisteet {p1.score}')
print(f'{p2.name} ({p2.location}) pisteet {p2.score}')
print(f'{p3.name} ({p3.location}) pisteet {p3.score}')

p1.print_info()
p2.print_info()
p3.print_info()

# olioviittausten tallentaminen listan muuttujien sijasta
players = []
# luodaan uusia pelaajia ja lisätään suoraan listalle
players.append(Player('Aku'))
players.append(Player('Aku'))
players.append(Player('Iines'))
players.append(Player('Roope'))
players.append(Player('Hannu'))
# sijoitetaan viittaukset olemassa oleviin pelaajaoliolistoihin listalle
players.append(p1)
players.append(p2)
players.append(p3)

# listan käsittely luupissa kuin ennenkin
for p in players:
    p.print_info()
    p.add_score()
    print('----------')


for p in players:
    p.print_info()