
# 作業履歴

* rails 最初の1歩
 - http://qiita.com/youcune/items/222777415f00d19cccb4
* config/route -> root 'welcome#index' -> controller/welcome_controller.rb
* config/route -> namespace :api -> namespace :v1 -> resource articles
* mkdir -p app/controllers/api/v1
* app/controllers/api/v1/articles_controller.rb  def index, def show
* render :json => object
* response.headers['X-MyApp-Version'] = '1.3'
* render :json => ret, :status => 400
* added gem 'rspec-rails'
* bundle exec rails generate rspec:install
* bundle exec rspec -> no test
* rm -rf test/

