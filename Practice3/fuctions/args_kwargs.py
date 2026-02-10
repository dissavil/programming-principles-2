def build_profile(*skills, **info):
    return {
        "skills": skills,
        "info": info
    }

profile = build_profile("python", "git", name="Dias", age=18)
print(profile)
