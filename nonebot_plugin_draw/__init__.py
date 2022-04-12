import random
import time
from nonebot.params import ArgPlainText
from nonebot import on_command
from .message import message_result ,message_sign

command = on_command('关帝灵签', priority=6)
@command.handle()
async def lq_():
    await command.send(
        message="一阵眩目后,你跪坐在卜筶杯前,向关帝祷告后,看着眼前的筶杯,你附身捧起杯珓,轻轻掷出...\n请输入'抛杯'"
    )

@command.got("pb")
async def pq_(reply: str = ArgPlainText('pb')):
    if reply == '抛杯':
        for i in range(3):
            a = random.randint(0,100)
            if a >= 15 :
                pd=True
                await command.send(
                    message=f"{random.choice(message_result)}"

                )
            else:#为了模拟真实抛杯才设置笑杯，纯属搞笑，可以删去
                await command.send(
                    message="你掷出了笑杯,此签不灵,请重新抽签",
                    at_sender=True,
                )
                pd=False
                break
            time.sleep(1)
        if pd is True:
            await command.send(
                message="\n掷出三次圣杯,灵签已现\n请输入'解签'",
                at_sender=True,
            )
        else:
           await command.finish()
    else:
        await command.finish('\n"成事在人不在天,这签不抽也罢" 于是你放下占杯,起身向关帝一拜,拂袖离去\n抽签结束',
                             at_sender=True,
            )

@command.got("jb")
async def pq_(re: str = ArgPlainText('jb')):
    if re=='解签':
        await command.finish(message=f"\n{random.choice(message_sign)}",at_sender=True)
    else:
        await command.finish('\n你想,"抽签只不过是寻求心理慰藉罢了,成事在人,不解又何妨?"于是你起身向关帝一拜,拂袖离去\n抽签结束',
                             at_sender=True,
                             )



