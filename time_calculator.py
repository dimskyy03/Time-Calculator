def add_time(start, duration, day = '') :
  period_dic = ['AM', 'PM']
  #start
  waktu, period = start.split()
  jam_awal, menit_awal = waktu.split(':')
  #

  #duration
  tambah_jam, tambah_menit = duration.split(':')
  #

  #list hari
  day_list = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
  number_day = {', Monday': 1, ', Tuesday': 2, ', Wednesday': 3, ', Thursday': 4, ', Friday': 5, ', Saturday': 6, ', Sunday': 7}
  #

  keterangan = 0
  #penambahan menit
  jam_add = int(jam_awal)
  menit_add = int(menit_awal)
  for i in range(int(tambah_menit)) :
    menit_add += 1
    if menit_add > 59 :
      menit_add = 0
      jam_add += 1
      if jam_add > 11 and period == 'PM' :
        period = 'AM'
        keterangan += 1
      elif jam_add > 11 and period == 'AM' :
        period = period_dic[1]
  #

  #penambahan jam
  for i in range(int(tambah_jam)) :
    jam_add += 1
    if jam_add > 12 :
      jam_add = 1
    if jam_add > 11 and period == 'PM' :
      period = 'AM'
      keterangan += 1
    elif jam_add > 11 and period == 'AM' :
      period = period_dic[1]
  #

  if keterangan == 0 :
    jumlah_hari = ''
  elif keterangan == 1 :
    jumlah_hari = '(next day)'
  elif keterangan > 1 :
    jumlah_hari = '(' + str(keterangan) + ' days later' + ')'


  menit_akhir = ('%0.2d' % menit_add)
  jam_akhir = str(jam_add)

  tambah_hari = 0
  if day != '' :
    for i in day_list :
      if day.casefold() == day_list[i].casefold() :
        day = day_list[i]
        break

    if keterangan == 0 :
      day = ', ' + day
    elif keterangan > 0 :
      day = ', ' + day
      for i in range(keterangan + number_day[day]) :
        tambah_hari += 1
        if tambah_hari > 7 :
          tambah_hari = 1
        day = ', ' + day_list[tambah_hari]

  new_time = jam_akhir + ":" + menit_akhir + ' ' + period + day + ' ' + jumlah_hari

  return new_time