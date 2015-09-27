# coding: utf-8

aaa = [1,[10,11,[100,101,102]],3]
ret = []

hoge(ret, aaa, 0)
ret.each do |rr|
  puts "*#{rr}*"
end

BEGIN {
  def hoge(r, a, depth)
    a.each do |x|
      if x.class == Fixnum
        r.push(" "*depth + x.to_s)
      else
        hoge(r, x, depth+1)
      end
    end
  end
}
