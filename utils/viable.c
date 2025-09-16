// viable.c
#include <stdio.h>

// Initializes any system-level settings (stub for now)
void initialize_system() {
    // Future setup logic can go here
    printf("System initialized.\n");
}

// Computes a meme score based on rarity and engagement
int meme_score(int rarity, int engagement) {
    if (rarity < 0 || engagement < 0) {
        return 0; // Prevent negative scores
    }
    return rarity * engagement;
}

// Sets aeration level (stub for now)
void set_aeration(int level) {
    // Placeholder for environmental tuning
    printf("Aeration level set to %d\n", level);
}
