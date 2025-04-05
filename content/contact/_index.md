---
title: 'Contact'
menu: navbar
type: 'blank'
bookcase_cover_src: 'icons/catalogue.svg'
bookcase_cover_src_dark: 'icons/catalogue_dark.svg'
weight: 10
---

## Send me new material to upload or send your feedback, I'd love to hear it
---

<div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px; flex-wrap: wrap;">

  <a href="https://www.youtube.com/channel/UC-O1ZI3h_W9kFRK5ANMREOg" target="_blank" class="social-btn youtube">
    <i class="fa-brands fa-youtube"></i> YouTube
  </a>

  <a href="https://instagram.com/lucasgouveamusic" target="_blank" class="social-btn instagram">
    <i class="fa-brands fa-instagram"></i> Instagram
  </a>

  <a href="https://github.com/ltgouvea" target="_blank" class="social-btn github">
    <i class="fa-brands fa-github"></i> GitHub
  </a>

  <button class="social-btn email" onclick="sendEmail()">
    <i class="fa-regular fa-envelope"></i> Send Email
  </button>

</div>

<style>
  .social-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 14px 28px;
    border: none;
    border-radius: 10px;
    font-family: 'Segoe UI', sans-serif;
    font-size: 16px;
    font-weight: 500;
    text-decoration: none;
    color: white;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    min-width: 150px;
  }

  .social-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2);
  }

  .social-btn.youtube {
    background-color: #cc0000;
  }

  .social-btn.instagram {
    background: linear-gradient(45deg, #c13584, #e1306c);
  }

  .social-btn.github {
    background-color: #24292e;
  }

  .social-btn.email {
    background-color: #2ecc71;
  }
</style>

<script>
function sendEmail() {
  window.location.href = "mailto:k2.wav.contact@gmail.com";
}
</script>
