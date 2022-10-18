<!DOCTYPE html>
<html>
<head>
  <style>
    <?php include 'find_face.css';?>
  </style>
</head>
<body>
<div class="form">
  <form action="find_face.py">
      <div class="title">Find the face</div>
      <div class="input-container ic1">
        <input id="filename" name="filename" class="input" type="file" placeholder=" " />
        <div class="cut"></div>
        <label for="filename" class="placeholder">File Name</label>
      </div>

      <div class="submit-container">
      <button type="text" class="submit">Find</button>
      </div>
</form>
</div>


</body>
</html>