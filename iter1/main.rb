OFFSETS = [ 
  [-1, -1], [0, -1], [1, -1],
  [-1, 0],  [1, 0],
  [-1, 1], [0, 1], [1, 1]
]

def outside?(i, j, maxi, maxj)
	i < 0 || j < 0 || i >= maxi || j >= maxj
end

def open_field(a, i, j)
	return '*' if a[i][j] == '*'
	count = 0
	OFFSETS.each do | di, dj |
		ni = i + di
		nj = j + dj
		next if outside?(ni, nj, a.size, a[i].size)
		count += 1 if a[ni][nj] == '*'
	end
	count.to_s
end

a = File.open('input.in').each_line.map(&:strip)

res = []
File.open("output.out",  "w+") do |f|
  a.each_with_index do | line, i |
	line.chars.each_with_index do | symb, j |
		f << open_field(a, i, j)
	end
	f.puts
  end
end

puts `cat output.out`