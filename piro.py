import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_wins = 0
        self.table = [[],[],[]]
    
    def __str__(self) -> str:
        return f"{self.name}"


class Game:
    def __init__(self):
        self.players = [] # 유저들의 목록
        self.deck = [i for i in range(1, 10)] # 숫자 생성
        self.players.append(Player("노영진"))
        self.players.append(Player("민세원"))
        self.players.append(Player("안정근"))


    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        # TODO 1 : 사용자로부터 이름을 입력받아 my_player에 저장해주세요.
        print("당신의 이름을 입력해주세요. (홍길동) :", end = "")
        self.my_player = input()
        self.players.append(Player(self.my_player))
        ##### END OF TODO 1 (문제와 본 라인 사이에 코드를 작성하세요.) #####


    def set_play_order(self, round_num):
        """ 
        - [ 게임 진행 ] 부분에서 게임진행 순서를 정하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """
        # TODO 2-(1) : 게임진행을 위한 플레이어를 재정렬해주세요.(ROUND 1 : 사전 순서로 이름을 오름차순으로 정렬, ROUND 2,3,4 : 점수를 기준으로 오름차순 정렬)
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        # Write code here..
        if round_num == 1:
            self.players.sort(key= lambda player : player.name)
            
        else:
            self.players.sort(key= lambda player : player.score)
        ##### END OF TODO 2-(1) (문제와 본 라인 사이에 코드를 작성하세요.) #####


        # TODO 2-(2) : 랜덤으로 1부터 9 사이의 숫자를 각 플레이어의 table에 저장해주세요 (3*3의 2차원 배열)
        # random에 대한 함수를 공부해봅시다.
        # Write code here..
        for player in self.players:
            tmp = [[],[],[]]
            numbers = list(range(1, 10))  # 1부터 9까지의 숫자 리스트를 생성
            random.shuffle(numbers)  # 숫자를 무작위로 섞음
            for i in range(9):
                tmp[(i//3)].append(numbers[i])  # 2차원배열에 숫자 배정
            player.table = tmp
        ##### END OF TODO 2-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####


    def check(self, player):
        """ 
        - [ 게임 진행 ] player의 빙고 개수를 확인하는 함수입니다.
        - 동일 클래스의 bingo()에서 호출됩니다.
        """
        bingo = 0
        c = player.table
        # 가로 확인
        for x in c: 
            if x.count(0) == 3:
                bingo += 1

        # TODO 4-(2) : 나머지 경우의 빙고를 확인하는 코드를 작성해주세요.
        # 세로 확인
        for i in range(3): 
            y = 0
            for j in range(3):
                if c[j][i] == 0:
                    y += 1
                    
            if y == 3:
                bingo += 1

        # 왼쪽위부터 시작하는 대각선 확인
        d1 = 0
        for i in range(3):
            if c[i][i] == 0:
                d1 += 1
        
        if d1 == 3:
            bingo += 1

        # 오른쪽위부터 시작하는 대각선 확인
        d2 = 0
        for i in range(3):
            if c[i][2-i] == 0:
                d2 += 1
        
        if d2 == 3:
            bingo += 1
        ##### END OF TODO 4-(2) (문제와 본 라인 사이에 코드를 작성하세요.) #####

        return bingo 
    

    def bingo(self):
        """ 
        - [ 게임 진행 ] 게임 진행의 핵심 함수입니다.
        - 동일 클래스의 play_round()에서 호출됩니다.

        - 1. 섞인 self.deck으로부터 숫자 하나를 뽑습니다.
        - 2. 각 플레이어의 table에서 해당하는 숫자를 지웁니다. (0으로 설정)
        - 3. 빙고 3개를 달성할 때까지 반복합니다.
        - 4. 빙고 3개에 성공한 플레이어를 winner 리스트에 추가합니다. (중복 가능)
        - 5. 이번 라운드에서 빙고를 달성한 winner 리스트와 점수를 반환합니다.

        - 주의사항
        - 빙고를 체크할 때 위의 check() 함수를 이용해서 체크해주세요.
        - check() 함수를 완성시키는 것이 TODO 4-(2) 문제입니다.
        """

        winner = []
        # TODO 4-(1) : 1 ~ 4 의 내용을 구현해주세요.
        for i in range(9):
            for player in self.players:
                for x in range(3):
                    for y in range(3):
                        if self.deck[i] == player.table[x][y]:
                            player.table[x][y] = 0

                result = self.check(player)
                if result >= 3:
                    winner.append(player)
            if winner:
                break
        ##### END OF TODO 4-(1) (문제와 본 라인 사이에 코드를 작성하세요.) #####
            
        # TODO 4-(3) : 플레이어의 이름과 현재 점수, table을 출력하는 코드를 작성해주세요.
        for player in self.players:
            print(f'>> {player} (현재 점수: {player.score})')
            for line in player.table:
                print(line)
            print()
        ##### END OF TODO 4-(3) (문제와 본 라인 사이에 코드를 작성하세요.) #####

        # 점수 계산 방식 : 승리했을 때 지운 숫자 개수가 점수가 됩니다.
        return (winner, i+1)
        

    def play_round(self):
        """
        - [ 게임 진행 ] 라운드 진행을 담당하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """
        
        play_order = ",".join(map(str, self.players))

        print(f"게임은 {play_order} 순으로 진행됩니다.\n")

        # TODO 3-(1) : 카드를 뽑기 전에 self.deck을 랜덤으로 섞어주세요.
        random.shuffle(self.deck)
        ##### END OF TODO 3-(1) (문제와 본 라인 사이에 코드를 작성하세요.) #####
        print("===========플레이어의 빙고 카드============")
        # TODO 3-(2) : 게임 진행의 핵심 함수입니다.
        winner, score = self.bingo()
        ##### END OF TODO 3-(2) ( self.bingo() 를 완성시켜주세요. ) ##### 
        
        # TODO 3-(3) : bingo() 함수의 결과를 플레이어 점수에 반영하는 코드를 작성해주세요.
        # 승리한 플레이어의 경우 round_wins도 1 증가시켜주세요.
        
        for player in winner:
            player.round_wins += 1
            player.score += score
            print(f'>>>> {player}님이 {score} 점을 얻었습니다 \^_^/ <<<<')
        print()

        ##### END OF TODO 3-(3) (문제와 본 라인 사이에 코드를 작성하세요.) ##### 

    def play_game(self):
        
        """
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        for round_num in range(1, 5):

          self.set_play_order(round_num)


          print("===========================")
          print(f"     ROUND {round_num} - START")
          print("===========================")
          self.play_round()

          
          print("===========================")
          print(f"     ROUND {round_num} - END")
          print("===========================")
          # 라운드 종료 후 각 플레이어들의 현재 점수
          for order, player in enumerate(self.players, 1): 
            print(f"{order}. {player} : {player.score}점")
          print()
    
    def game_result(self):
        
        # TODO 5-(1) : 점수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 점수")
        print("=============================")
        self.players.sort(key=lambda player: (-player.score, player.name))
        for rank, player in enumerate(self.players, 1):
            if player.name == self.my_player:
                print(f'{rank}등 - *{player}* : {player.score}점')
            else:
                print(f'{rank}등 - {player} : {player.score}점')
            #출력
            ...
        # Write code here..
        ##### END OF TODO 5-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        
  
        # TODO 5-(2) : 승리 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 승리 횟수")
        print("=============================")
        self.players.sort(key=lambda player: (-player.round_wins, player.name))
        for rank, player in enumerate(self.players, 1):
            if player.name == self.my_player:
                print(f'{rank}등 - *{player}* : {player.round_wins}번')
            else:
                print(f'{rank}등 - {player} : {player.round_wins}번')
            ...
        self.players.sort(key=lambda player: (-player.score, -player.round_wins))
        # Write code here..
        ##### END OF TODO 5-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

          
    def game(self):
        
        """
        - 게임 운영을 위한 함수입니다. 
        - 별도의 코드 작성이 필요 없습니다. 
        """

        self.start_game()
        self.play_game()
        self.game_result()


if __name__ == "__main__":  
    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()

    game.game()