require 'rails_helper'

RSpec.describe "welcome page", :type => :request do
  it "first test" do
    get "/"
    expect(response).to be_success
    expect(response).to have_http_status(200)
  end

  it "welcome page test: custom http request header" do
    get "/", nil, {'X-Foo'=>'10'}
    expect(response).to be_success
    expect(response.body).to eq('<h1>Welcome page</h1>')
  end

end
