with open('trans.txt') as open_file:
    all_data = open_file.read()

# �e�s�̃��X�g�����
line_list = all_data.splitlines()

#�ǂݍ��񂾃f�[�^�������ɒǉ�����
bot_dict = {}

for line in line_list:
    orig,trans = line.split(':')
    bot_dict[orig] = trans

print(bot_dict)