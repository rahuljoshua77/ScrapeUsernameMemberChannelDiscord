import discum
import config,time
from discum.gateway.session import guild

guild_id = config.guildId
channel_id = config.channelId
bot = discum.Client(token=config.tokenAcc)
bot.gateway.fetchMembers(guild_id, channel_id, keep=['username','discriminator','premium_since'],startIndex=0, method='overlap',wait=1)
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

with open('result.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        #temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        #creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        #if temp != None:
            #z = __get_badges(temp)
            #if len(z) != 0:
                #badges = ', '.join(z)
        print(f'ID: @{id} | Username: {username}')
        file.write(f'ID: @{id} | Username: {username}\n')
