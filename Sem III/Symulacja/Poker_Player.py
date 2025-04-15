from Poker_Funcs import Poker_odds_calculator
import random


class Player:
    
    def __init__(self, 
                 money : int,
                 cards = None,
                 recklessness : float = 0, 
                 profligacy : float = 0.1, 
                 payed : int = 0,
                 expected_hand = 'Straight',
                 ) -> None:
        self.money = money
        self.cards = cards
        self.payed = payed
        self.recklessness = recklessness
        self.profligacy = profligacy
        self.allin = False
        self.expected_hand = expected_hand
    
    def player_decision_based_on_pot(self, pot, raising_ceiling = 0.1, calling_ceiling = 0.8):
        """
        Funkcja decydująca, czy gracz powinien spasować, czy podbić w zależności od puli.
        :param player: Gracz (obiekt klasy Player).
        :param pot: Pula gry (ilość żetonów w puli).
        :param a: Procent stacka gracza, poniżej którego gracz podbija (domyślnie 50%).
        :param b: Procent stacka gracza, powyżej którego gracz pasuje (domyślnie 80%).
        :return: 'fold' jeśli gracz spasuje, 'call' jeśli sprawdzi, 'raise' jeśli podbije.
        """
   

        # Jeśli pula przekracza wartość b (np. 80% stacka), gracz spasuje
        if pot > calling_ceiling * self.money:
            return 0
        # Jeśli pula jest pomiędzy a (np. 50%) a b (np. 80%), gracz sprawdza
        elif calling_ceiling * self.money >= pot >= raising_ceiling * self.money:
            return 1
        # Jeśli pula jest mniejsza niż a (np. 50%), gracz podbija
        elif pot < raising_ceiling * self.money:
            return 2
    
    def is_still_playing(self,table_cards, min_chance : float = 0.5) -> bool:
        
        min_hand = self.expected_hand
        
        hands = ['High card', 'One pair', 'Two pair', 'Three-of-a-Kind', 'Straight', 'Flush', 'Full house', 'Four-of-a-Kind', 'Straight flush']
        odds = 0
        my_odds = Poker_odds_calculator(self.cards,table_cards)
        
        for i in range(hands.index(min_hand),len(hands)):
            odds += my_odds[hands[i]]
        
        
        if odds > min_chance:
            return 1
        else: 
            return 0
            
    def decision(self,choice,current_bet):
        if self.money<=0: return ("fold",0)
        else:
            match choice:
                case(0):
                    return ("fold",0)
                case(1):
                    return ("call",0)
                case(2):
                    return ("call",0)
                case(3):
                    amount = min(int(self.profligacy * 0.5 * self.money),self.money)
                    if amount + self.payed <= current_bet: 
                        amount = min(current_bet - self.payed + 20,self.money)
                        if amount == self.money:
                            self.allin = True
                    return ('raise', amount)
                case(4):
                    amount = min(int(self.profligacy * 2 * self.money),self.money)
                    if amount + self.payed <= current_bet: 
                        amount = min(current_bet - self.payed + 20,self.money)
                        if amount == self.money:
                            self.allin = True
                    return ('raise', amount)
                   
        
class AveragePlayer(Player):
    def __init__(self, money : int,cards = None, recklessness : float = 0.2, profligacy : float = 0.3, payed : int = 0, expected_hand = 'Straight') -> None:
        super().__init__(money,cards, recklessness, profligacy, payed,expected_hand)
        
    
    def action(self,table_cards,pot,round,current_bet):
        
        raising_ceiling = self.profligacy / 2
        calling_ceiling = min(self.profligacy * 2, 1)
        
        choice = self.is_still_playing(table_cards, 0.4 + 0.1 * round) + self.player_decision_based_on_pot(pot,raising_ceiling = raising_ceiling, calling_ceiling= calling_ceiling)
        if random.random() < self.recklessness: choice +=1
        
        return self.decision(choice,current_bet)
 
class ConsistentPlayer(Player):
    def __init__(self, money : int,cards = None, recklessness : float = 0, profligacy : float = 0.1, payed : int = 0, expected_hand = 'Straight') -> None:
        super().__init__(money,cards, recklessness, profligacy, payed,expected_hand)
        
    def action(self,table_cards,pot, round,current_bet):
        

        raising_ceiling = self.profligacy / 2
        calling_ceiling = min(self.profligacy * 2, 1)
        
        choice = self.is_still_playing(table_cards, 0.4 + 0.1 * round) + self.player_decision_based_on_pot(pot,raising_ceiling = raising_ceiling, calling_ceiling= calling_ceiling)
        
        if round > 1:
            choice += 1
        
        elif random.random() < self.recklessness: choice +=1
        
        
        return self.decision(choice,current_bet)
  
class PatientPlayer(Player):
    def __init__(self, money : int,cards = None, recklessness : float = 0, profligacy : float = 0.1, payed : int = 0, expected_hand = 'Straight') -> None:
        super().__init__(money,cards, recklessness, profligacy, payed,expected_hand)
        
    def action(self,table_cards,pot, round,current_bet):
        
        raising_ceiling = self.profligacy / 2
        calling_ceiling = min(self.profligacy * 2, 1)
        
        
            
        
        choice = self.is_still_playing(table_cards, 0.4 + 0.1 * round) + self.player_decision_based_on_pot(pot,raising_ceiling = raising_ceiling, calling_ceiling= calling_ceiling)
        
        if round < 3:
            choice = 1
        
        elif random.random() < self.recklessness: choice +=1
        
        return self.decision(choice,current_bet)
  
class PassivePlayer(Player):
    def __init__(self, money : int,cards = None, recklessness : float = 0, profligacy : float = 0.1, payed : int = 0, expected_hand = 'Straight') -> None:
        super().__init__(money,cards, recklessness, profligacy, payed,expected_hand)
        
    def action(self,table_cards,pot, round,current_bet):
        
        raising_ceiling = self.profligacy / 2
        calling_ceiling = min(self.profligacy * 2, 1)
        
        choice = self.is_still_playing(table_cards, 0.4 + 0.1 * round) + self.player_decision_based_on_pot(pot,raising_ceiling = raising_ceiling, calling_ceiling= calling_ceiling)
        
        if choice != 0: 
            choice = 1
        
        
        return self.decision(choice,current_bet)

class AgressivePlayer(Player):
    def __init__(self, money : int,cards = None, recklessness : float = 0, profligacy : float = 0.1, payed : int = 0, expected_hand = 'Straight') -> None:
        super().__init__(money,cards, recklessness, profligacy, payed,expected_hand)
        
    def action(self,table_cards,pot, round,current_bet):
        
        raising_ceiling = self.profligacy / 2
        calling_ceiling = min(self.profligacy * 2, 1)
        
        
            
        
        choice = self.is_still_playing(table_cards, 0.4 + 0.1 * round) + self.player_decision_based_on_pot(pot,raising_ceiling = raising_ceiling, calling_ceiling= calling_ceiling)
        
        if choice in [1,2]:
            if random.random() < 0.8: choice += 1
        
        if random.random() < self.recklessness: choice +=1
    
        return self.decision(choice,current_bet)
  
                  
class BettingManager:
    def __init__(self, players, small_blind=25, big_blind=50):
        """ 
        Zarządza pieniędzmi i zakładami w grze.
        :param players: Lista obiektów klasy Player reprezentujących graczy.
        :param small_blind: Kwota small blind.
        :param big_blind: Kwota big blind.
        """
        self.players = players
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.pot = 0  # Pula gry
        self.current_bet = big_blind  # Aktualna stawka w rundzie
        self.active_players = list(range(len(players)))  # Indeksy graczy, którzy nadal grają

    def post_blinds(self):
        """
        Wymusza wpłacenie small blind i big blind przez dwóch pierwszych aktywnych graczy.
        """
        index = random.sample(self.active_players,2)
        small_blind_player = index[0]
        big_blind_player = index[1]

        self.small_blind = min(self.small_blind, self.players[small_blind_player].money)
        self.big_blind = min(self.big_blind, self.players[big_blind_player].money)
        
        self.players[small_blind_player].money -= self.small_blind
        self.players[big_blind_player].money -= self.big_blind

        self.pot += self.small_blind + self.big_blind

        
        self.players[small_blind_player].payed = self.small_blind
        self.players[big_blind_player].payed = self.big_blind
        

    def player_action(self, player_index, action, raise_amount):
        """
        Obsługuje decyzję gracza.
        :param player_index: Indeks gracza.
        :param action: 'fold', 'call', 'raise'.
        :param raise_amount: Kwota podbicia (dla 'raise').
        """
        player = self.players[player_index]
        # raise_amount += self.current_bet - player.payed


        if player.allin:
            player.payed += player.money
            self.pot += player.money
            player.money = 0
            self.current_bet = max(player.payed,self.current_bet)
            player.payed =  self.current_bet
        
        elif action == "fold":
            self.active_players.remove(player_index)
            player.payed = 0

        elif action == "call":
            call_amount = self.current_bet
            
            
            player.money -= call_amount - player.payed
            self.pot += call_amount - player.payed
            player.payed = call_amount
           
        

        elif action == "raise":
            if raise_amount+player.payed <= self.current_bet:
                raise ValueError("Kwota podbicia musi być większa niż aktualna stawka.")
            
            if player.money < 0: print("TUTAJ", "1")
            player.money -= raise_amount #- player.payed
            self.pot += raise_amount  #- player.payed
            player.payed += raise_amount
            self.current_bet = player.payed
            if player.money < 0: print("TUTAJ", "2")
        

    def distribute_winnings(self, winning_player_index, tie = False):
        """
        Rozdziela wygraną w rundzie pomiędzy zwycięzców.
        :param winning_player_index: Indeks gracza, który wygrał.
        """
        if tie:
            for i in winning_player_index:
                winner = self.players[int(i)-1]
                winner.money += self.pot//len(winning_player_index)  # Dodaje wygraną do pieniędzy gracza
                # print(f"Gracz {int(i)} wygrywa {self.pot//len(winning_player_index)} żetonów.")
        
        else:
            winner = self.players[winning_player_index-1]
            winner.money += self.pot  # Dodaje wygraną do pieniędzy gracza
            # print(f"Gracz {winning_player_index} wygrywa {self.pot} żetonów.")
            
        self.pot = 0  # Resetuje pulę po rozdaniu
        for player in self.players:
            player.payed = 0
            player.allin = False
            if player.money < 0: player.money = 0

    def show_status(self):
        """
        Wyświetla aktualny status graczy i puli.
        """
        print("\n=== Status gry ===")
        for i, player in enumerate(self.players):
            status = "aktywny" if i in self.active_players else "nieaktywny"
            print(f"Gracz {i + 1}: {player.money} żetonów ({status})")
        print(f"Pula: {self.pot}\n")
        
    def get_player_money(self):
        return self.players[0].money
    
    
    def add_money_for_player(self, player_index, amount):
        self.players[player_index].money += amount