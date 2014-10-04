class WelcomeController < ApplicationController
  def index
    if request.headers['X-Foo']
      render :text => '<h1>Welcome page</h1>'
    else
      render :text => '<h1>Welcome page2</h1>'
    end
  end
end
