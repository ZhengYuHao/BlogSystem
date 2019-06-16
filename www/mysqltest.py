# import orm
# import model
# import asyncio
# async  def test(loop):
#     await orm.create_pool(loop=loop,user='www-data', password='password', db='awesome')
#     print("Here")
#     u = model.User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#
#     await u.save()
# #
# # for x in test():
# #     pass
#
#
# #
# # import orm
#
# # import model
# #
# # async def test(loop):
# #     await orm.create_pool(loop=loop, user='lxp', password='onlinetrader', db='awesome')
# #     u = model.User(name='Test', email='lxp@exa22mple.com', passwd='1234567890', image='about:blank')
# #     await u.save()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.run_forever()
import orm
import asyncio
import model

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='password', db='awesome')
    u = model.User(name='Test', email='test2@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    ## 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()