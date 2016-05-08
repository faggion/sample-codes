require 'twitter'

p ARGV

client = Twitter::REST::Client.new do |config|
  config.consumer_key        = ARGV[0]
  config.consumer_secret     = ARGV[1]
  config.access_token        = ARGV[2]
  config.access_token_secret = ARGV[3]
end

#client.home_timeline.each do |tw|
client.list_timeline(727030702030475264).each do |tw|
  #p "#{tw.user.name}, #{tw.user.friends_count}, #{tw.user.tweets_count}, #{tw.user.screen_name}, #{tw.user.followers_count}: #{tw.text}"
  p "#{tw.user.name}, #{tw.text}"
  if tw.media.count > 0
    p "media count -> #{tw.media.count}"
    tw.media.each do |m|
      if m.class == Twitter::Media::Photo
        p "photo is -> #{m.media_uri}"
      else
        p "unknown type -> #{m}"
      end
    end
  end
end
