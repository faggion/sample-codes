class Api::V1::ArticlesController < ApplicationController
  def index
    render :text => '<h1>Welcome articles</h1>'
  end

  def show
    response.headers['X-MyApp-Version'] = '1.3'
    ret = {
      id: params[:id].to_i,
      name: 'foo',
      age: 25,
    }
    render :json => ret, :status => 400
  end
end
