function on_register(form, url) {
  if (form.elements['username'] != form.elements['confirm_password']) {
    info = document.getElementById('confirm_password_info')
    info.innerText = 'Passwords do not match!'
    return false;
  }
  formData = new FormData()
  formData.append('email_address', form.elements['email_address'].value)
  formData.append('username', form.elements['username'].value)
  formData.append('password', form.elements['password'].value)
  axios({
    url: url,
    method: 'POST',
    data: formData,
  })
  return false;
}
