<!DOCTYPE html>
<html>
<head>
  <style>
    <?php include 'reg_face.css';?>
  </style>
</head>
<body>
<div class="form">
  <form action="reg_db.py">
      <div class="title">Face Registration</div>
      <div class="input-container ic1">
        <input id="cid" name="cid" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="cid" class="placeholder">Criminal Id</label>
      </div>

      <div class="input-container ic2">
        <input id="name" name="name" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="name" class="placeholder">Full Name</label>
      </div>

      <div class="input-container ic2">
        <input id="phone" name="phone" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="phone" class="placeholder">Contact</label>
      </div>

      <div class="input-container ic2">
        <input id="address" name="address" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="address" class="placeholder">Address</label>
      </div>

      <div class="input-container ic2">
        <select id="gender" name="gender" class="input" type="text" placeholder=" " >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
        <div class="cut"></div>
        <label for="gender" class="placeholder">Gender</label>
      </div>

      <div class="input-container ic2">
        <input id="dob" name="dob" class="input" type="date" placeholder=" " />
        <div class="cut"></div>
        <label for="dob" class="placeholder">DOB</label>
      </div>

      <div class="input-container ic2">
        <input id="height" name="height" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="height" class="placeholder">Height(fts)</label>
      </div>

      <div class="input-container ic2">
        <input id="nationality" name="nationality" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="nationality" class="placeholder">Nationality</label>
      </div>

      <div class="input-container ic2">
        <input id="offence" name="offence" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="offence" class="placeholder">Offence</label>
      </div>

      <div class="input-container ic2">
        <input id="doa" name="doa" class="input" type="date" placeholder=" " />
        <div class="cut"></div>
        <label for="doa" class="placeholder">Date of arrest</label>
      </div>

      <div class="input-container ic2">
        <input id="place" name="place" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="place" class="placeholder">Place</label>
      </div>

      <div class="input-container ic2">
        <input id="officer" name="officer" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="officer" class="placeholder">Officer</label>
      </div>

      <div class="input-container ic2">
        <input id="filename" name="filename" class="input" type="file" placeholder=" " />
        <div class="cut"></div>
        <label for="filename" class="placeholder">File Name</label>
      </div>

      <div class="submit-container">
      <button type="text" class="submit">Register</button>
      </div>
</form><br><br><br><br><br><br><br><br>
</div>

</body>
</html>