---
title: 'Contact'
menu: navbar
type: 'blank'
bookcase_cover_src: 'fa-solid fa-paper-plane'
weight: 10
---

## Send me new material to upload or send your feedback, I'd love to hear it
---

<div class="social-btn-container">

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
  .social-btn-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
    margin-top: 40px;
    width: 100%;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    padding: 0 20px;
  }

  .social-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 16px 32px;
    width: 100%;
    border: none;
    border-radius: 12px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 18px;
    font-weight: 600;
    text-decoration: none;
    color: white;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
  }

  .social-btn:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
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

  @media screen and (max-width: 480px) {
    .social-btn {
      font-size: 16px;
      padding: 14px 24px;
    }
  }
</style>

<script>
function sendEmail() {
  window.location.href = "mailto:k2.wav.contact@gmail.com";
}
</script>
