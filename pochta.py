strings = ['Hello Emma it"s Mark how are u, i need your help!',
           'Hello Marty it"s Mark how are u, i need your help!',
          'Hello Mark it"s Mark how are u, i need your help!',
          'Sales! Li-ning sales!','Buy Right now',
           'Hello Emma, how do u do?Im gonna invite u to restaurant',
           'Hello Emma how are u? Have a nice day',
           'EMMA SOS!!! Production is down','Sales in Nike shop',
           'Emma hello, help me pls',
           'Hi Emma, its Marty McFly i want invite u to time-travel',
           'Hi, Emma, please, need to meet']
def write_to(strings):
        with open('message1.txt','a') as file1:
            for sentence in strings:
                file1.write(sentence + '\n')
write_to(strings)


