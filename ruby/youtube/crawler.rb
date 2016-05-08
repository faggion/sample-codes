# coding: utf-8
require 'net/http'
require 'uri'
require 'json'
require 'cgi/util'
require 'fileutils'

OUTPUT_DIR = '/tmp/youtube'
WORDS = ['犬 赤ちゃん おもしろ',
         '犬 赤ちゃん かわいい',
         '犬 かわいい',
         '犬 感動',
         '犬 仲良し',
         '猫 赤ちゃん おもしろ',
         '猫 赤ちゃん かわいい',
         '猫 かわいい',
         '猫 感動',
         '猫 仲良し']
MAX_RESULTS = 50
API_KEY     = "***"
BASE_SEARCH = "https://www.googleapis.com/youtube/v3/search?part=snippet&key=#{API_KEY}&type=video&order=viewCount&maxResults=#{MAX_RESULTS}&q="
BASE_DETAIL = "https://www.googleapis.com/youtube/v3/videos?part=statistics&key=#{API_KEY}&id="

def api_search(w, r)
  api_url = BASE_SEARCH + CGI.escape(w)
  STDERR.puts(api_url)
  ret = JSON.parse(Net::HTTP.get(URI.parse(api_url)))
  ids = []
  ret['items'].each do |i|
    if r[i['id']['videoId']] == nil
      r[i['id']['videoId']] = {'title'     => i['snippet']['title'],
                               'tags'      => w.split(' '),
                               'thumbnail' => i['snippet']['thumbnails'].fetch('high', i['snippet']['thumbnails']['default'])['url']}
    end
    ids.push(i['id']['videoId'])
  end
  ids
end

def api_detail(w, r, ixs)
  api_ids = []
  ixs.each do |ii|
    if r[ii]['viewCount'] == nil
      api_ids.push(ii)
    else
      STDERR.puts("id=#{ii}, org_tags=#{r[ii]['tags'].join(",")}, new_tags=#{w}")
      r[ii]['tags'] |= w.split(' ')
    end
  end

  if not api_ids.empty?
    api_url = BASE_DETAIL + CGI.escape(api_ids.join(","))
    STDERR.puts(api_url)
    ret = JSON.parse(Net::HTTP.get(URI.parse(api_url)))
    ret['items'].each do |i|
      r[i['id']]['viewCount'] = i['statistics'].fetch('viewCount', '0').to_i
      r[i['id']]['likeCount'] = i['statistics'].fetch('likeCount', '0').to_i
      r[i['id']]['dislikeCount'] = i['statistics'].fetch('dislikeCount', '0').to_i
    end
  end
end

def dump_json(r, root)
  File.write(root + '/data.json', JSON.pretty_generate(r))
end

results = {}
WORDS.each do |w|
  iii = api_search(w, results)
  api_detail(w, results, iii)
  sleep(0.3)
end
FileUtils.mkdir_p(OUTPUT_DIR)
dump_json(results, OUTPUT_DIR)

