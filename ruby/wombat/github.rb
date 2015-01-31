require 'wombat'

data = Wombat.crawl do
  base_url "https://www.github.com"
  path "/"

  headline xpath: "//h1"
  subheading css: "p.subheading"

  what_is({ css: ".one-half h3" }, :list)

  explore "xpath=//ul/li[4]/a" do |e|
    puts e
    e.gsub(/Explore/, "LOVE")
  end

  test1 "xpath=html/body/a" do |e|
    {hello: e}
  end
  test2 "xpath=/html/body/a" do |e|
    e
  end
  test3 "xpath=//body/a" do |e|
    e
  end
end

puts data
