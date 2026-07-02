from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-x9!@#k2m4n5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2g3h4i5j6k7l8m9n0o1p'

DEBUG = False

ALLOWED_HOSTS = ['melikasafari.runflare.run', 'localhost', '127.0.0.1', '*']


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gallery',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'music_blog.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gallery.context_processors.global_context',
            ],
        },
    },
]


WSGI_APPLICATION = 'music_blog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_TZ = True


STATIC_URL = '/public/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "public" / "static"


MEDIA_URL = '/public/media/'
MEDIA_ROOT = BASE_DIR / 'public' / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ─── Jazzmin ───────────────────────────────────────────────────────────────────

JAZZMIN_SETTINGS = {
    "custom_css": "admin_custom.css",
    "show_sidebar": False,
    # برندینگ
    "site_title": "گالری هنری",
    "site_header": "گالری هنری",
    "site_brand": "🎼 گالری",
    "welcome_sign": "به پنل مدیریت گالری خوش آمدید",
    "copyright": "گالری هنری © 2026",

    # منوی بالا
    "topmenu_links": [
        {"name": "🏠 مشاهده سایت", "url": "/", "new_window": True},
        {"name": "➕ پست جدید",    "url": "/admin/gallery/post/add/"},
        {"name": "🏷️ دسته‌بندی جدید", "url": "/admin/gallery/category/add/"},
    ],

    # منوی کاربر
    "usermenu_links": [
        {"name": "مشاهده سایت", "url": "/", "new_window": True},
    ],

    # آیکون‌ها
    "icons": {
        "auth":             "fas fa-shield-alt",
        "auth.user":        "fas fa-user-circle",
        "auth.group":       "fas fa-users",
        "gallery.post":     "fas fa-film",
        "gallery.category": "fas fa-layer-group",
        "gallery.artist":   "fas fa-music",
    },
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    # ترتیب sidebar
    "order_with_respect_to": [
        "gallery",
        "gallery.post",
        "gallery.category",
        "gallery.artist",
        "auth",
    ],

    # فرم‌ها
    "changeform_format": "horizontal_tabs",

    # جستجوی سریع روی پست
    "search_model": ["gallery.post", "gallery.artist"],

    "show_ui_builder": False,
    "related_modal_active": True,
    "navigation_expanded": True,
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    # تم پایه — تاریک و اشرافی
    "theme":           "cyborg",
    "dark_mode_theme": "cyborg",

    # navbar — تاریک با رنگ برند بنفش
    "navbar":          "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed":    True,
    "navbar_small_text": False,

    # sidebar — تاریک بنفش
    "sidebar":         "sidebar-dark-purple",
    "sidebar_fixed":   True,
    "sidebar_nav_flat_style":    False,
    "sidebar_nav_legacy_style":  False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_child_indent":  True,
    "sidebar_nav_small_text":    False,
    "sidebar_disable_expand":    False,

    # رنگ accent — طلایی/زرد برای contrast با بنفش
    "accent": "accent-warning",

    # برند
    "brand_colour":    "navbar-purple",
    "brand_small_text": False,

    # layout
    "layout_boxed":    False,
    "footer_fixed":    False,
    "body_small_text": False,
    "footer_small_text": True,

    # دکمه‌ها
    "button_classes": {
        "primary":   "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info":      "btn-outline-info",
        "warning":   "btn-warning",
        "danger":    "btn-outline-danger",
        "success":   "btn-outline-success",
    },
}
