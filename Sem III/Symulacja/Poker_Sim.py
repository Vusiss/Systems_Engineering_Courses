import random as r  
from Poker_Player import AveragePlayer, BettingManager
from Poker_Funcs import compare_hands,find_winning_player

def Poker_games(test_player ,n_players: int, n_games, money_for_player) -> None: 
    """
    Simulates a simplified poker game for a given number of players.
    :param n_players: Number of players in the game.
    """
    players = [test_player]
    for i in range(n_players-1):
        players.append(AveragePlayer(money_for_player))
    
    ending_money=[]    
        
    for game in range(n_games):    
        
        # Initialize a deck of cards.
        card_colors = ['heart', 'spade', 'diamond', 'club']
        card_values = list(range(1, 14))  # Card values (1 = A, 11 = J, 12 = Q, 13 = K).
        deck = [(color, value) for color in card_colors for value in card_values]

        # Shuffle the deck.
        r.shuffle(deck)

        # Deal 3 community cards for the table.
        table_cards = deck[:2]
        del deck[:2]


        players_cards = {}
        
        for i in range(n_players):
            players[i].cards = deck[:2]
            players_cards[f'player {i+1}'] = players[i].cards
            del deck[:2]



        not_playing_players = []
        
        
        
        
        bettingManager = BettingManager(players)
        
        for i in bettingManager.active_players:
        
            active_player_money = players[i].money
            players[i].payed = 0
            if active_player_money <= 0:
                not_playing_players.append(i)
                bettingManager.active_players.remove(i)
                
        
        
        # Game rounds. 
        for round in range(3):
            table_cards.append(deck[0])
            del deck[0]
            if len(bettingManager.active_players) < 2:
                # print('Koniec gry')
                break
            bettingManager.post_blinds()
            
            betting_stage = True
            
            while betting_stage:
                for i in bettingManager.active_players:
                    
                    if players[i].money >= bettingManager.current_bet: player_action = players[i].action(table_cards,bettingManager.pot,round+1,bettingManager.current_bet)
                    else: player_action = ("fold",0)
                    bettingManager.player_action(i,player_action[0],raise_amount=player_action[1])
                    
                
                active_payed_values = [players[i].payed for i in bettingManager.active_players]
                
                
                if all(value == active_payed_values[0] for value in active_payed_values) if active_payed_values else True:
                    betting_stage == False
                    break
        
            
            for player in players:
                player.payed = 0
            
            # Compare hands and determine the winner.
            players_rank, players_best_hands = compare_hands(players, table_cards, n_players, not_playing_players)
            result, best_hand_, hand_description,winning_player = find_winning_player(players_rank, players_best_hands)

            for i in range(len(players)):
                if (i not in not_playing_players) and (i not in bettingManager.active_players): 
                    players_cards.pop(f'player {i + 1}')
                    not_playing_players.append(i)
                    if len(not_playing_players) == n_players-1:
              
                        players_rank, players_best_hands = compare_hands(players, table_cards, n_players, not_playing_players)
                        result, best_hand_, hand_description, winning_player = find_winning_player(players_rank, players_best_hands)
                      
                        bettingManager.distribute_winnings(winning_player)
                        
                        break
            
            
        
        
        if len(not_playing_players) != n_players-1:    

            if isinstance(winning_player,int): bettingManager.distribute_winnings(winning_player)
            else: bettingManager.distribute_winnings(winning_player,tie=True)

        ending_money.append(players[0].money)
            
    return ending_money

def simulation(PlayerObject,money,recklessness,profligacy,expected_hand):
    
    money_won = []
   
    test_player = PlayerObject(money = money, recklessness = recklessness, profligacy = profligacy, expected_hand = expected_hand)
    money_won = Poker_games(test_player,8,10,money_for_player = money)
    data = [PlayerObject.__name__,money,recklessness,profligacy,expected_hand] + money_won
     
        
    return data
    
 