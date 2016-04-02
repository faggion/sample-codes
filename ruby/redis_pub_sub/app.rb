require 'redis'
require 'logger'

logger = Logger.new("/tmp/subscriber.log")
def logger.write(msg)
  self << msg
end

redis_conn ||= Redis.new(:path => '/tmp/redis.sock')
redis_conn.subscribe("mych") do |on|
  on.message do |channel, msg|
    logger.info(channel)
    logger.info(msg)
    #sleep(1.0)
  end
end
